import pandas as pd
import multiprocessing
import numpy as np
import tqdm



def parallel_execution(user_id: list, tweets_filtered: pd.DataFrame, parent_stderr):
    processes, core_users, non_core_users = [], [], []
    sublist = np.array_split(user_id, 10)  # use number of CPU's core

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    process_id = 0

    for users_sublist in sublist:
        processes.append(multiprocessing.Process(target=get_core_users_parallel, args=(users_sublist, tweets_filtered, parent_stderr, process_id, return_dict)))
        process_id += 1

    print("Starting processes...\n")

    for process in processes:
        process.start()

    for process in processes:
        process.join()  # blocking call

    print("Collecting results...\n")

    for result in return_dict.values():
        core_users += result[0]
        non_core_users += result[1]

    return core_users, non_core_users


def get_core_users_parallel(users_activity_filtered, tweets_filtered, parent_stderr, process_id, return_dict):  # , old_users, new_users
    core_users = []
    non_core_users = []
    for user_id in tqdm.tqdm(users_activity_filtered, file=parent_stderr):
        parent_stderr.flush()

        activity_list = tweets_filtered.loc[tweets_filtered["user_id"] == str(user_id), :]
        activity_list = activity_list.sort_values(by="created_at")
        activity_list = activity_list.reset_index(drop=True)
        list_dates = activity_list["created_at"].tolist()
        # TODO: tune 90 days
        if (list_dates[-1] - list_dates[0]).days < 90:  # user active for less than 3 months => non core
            non_core_users.append(user_id)
            continue
        i = 0
        index_core_period = 0
        core_period = 0
        check = False
        while i < (len(list_dates) - 1):
            if (list_dates[i + 1] - list_dates[i]).days > 7:
                check = True
                core_period = max((list_dates[i] - list_dates[index_core_period]).days, core_period)
                index_core_period = i + 1
            i += 1
        if (not check) or (check and core_period >= 90):
            core_users.append(user_id)
        else:
            non_core_users.append(user_id)
    return_dict[process_id] = core_users, non_core_users


def get_core_user(users_activity_filtered, tweets_filtered): #, old_users, new_users
    core_users = []
    non_core_users = []
    for user_id in tqdm.tqdm(users_activity_filtered):
        activity_list = tweets_filtered.loc[tweets_filtered["user_id"] == str(user_id), :]
        activity_list = activity_list.sort_values(by="created_at")
        activity_list = activity_list.reset_index(drop=True)
        list_dates = activity_list["created_at"].tolist()
        # TO DO: tune this
        if (list_dates[-1] - list_dates[0]).days < 50:  # user active for less than 3 months => non core
            non_core_users.append(user_id)
            continue
        i = 0
        index_core_period = 0
        core_period = 0
        check = False
        while i < (len(list_dates) - 1):
            if (list_dates[i + 1] - list_dates[i]).days > 7:
                check = True
                core_period = max((list_dates[i] - list_dates[index_core_period]).days, core_period)
                index_core_period = i + 1
            i += 1
        if (not check) or (check and core_period >= 50):
            core_users.append(user_id)
        else:
            non_core_users.append(user_id)
    return core_users, non_core_users


if __name__ == '__main__':
    dateparse = lambda x: pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S%z")  # pd.datetime.strptime
    tweets = pd.read_csv("../data/sample_tweets.csv", #path/to/tweets_file
                         # nrows = 400000,
                         usecols=["tweet_id", "user_id", "created_at"],
                         parse_dates=['created_at'],
                         converters={"user_id": str,
                                     "tweet_id": str},
                         date_parser=dateparse,
                         lineterminator='\n')
    activity = pd.read_csv("../data/users_activity.csv", #path/to/activity_file/
                           converters={"user_id": str})
    users_activity_filtered = activity[activity["nbr_tweets_in_dataset"] >= 20].reset_index()[
        "user_id"].unique().tolist()  # TO DO: tune this
    tweets_filtered = tweets[tweets["user_id"].isin(users_activity_filtered)]

    users_activity_filtered = tweets_filtered["user_id"].unique().tolist()

    core_users, non_core_users = get_core_user(users_activity_filtered, tweets_filtered)

    df_core_users = pd.DataFrame(core_users, columns=["user_id"])
    df_non_core_users = pd.DataFrame(non_core_users, columns=["user_id"])

    df_core_users.to_csv("../data/core_users.csv", index=False)
    df_non_core_users.to_csv("../data/non_core_users.csv", index=False)