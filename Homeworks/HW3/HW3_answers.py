#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#Get access to API
auth = tweepy.OAuthHandler('99bJyQdvP6aHSAXtQbvXv3Ia7', 'gjen7dxOV8djaTQ6ig7Joe99coAPNbCXdzYe6AD9lWbcAnubUm')
auth.set_access_token('930848858-XCglhrhAm7eY60n4avt72iE5pdcBc725wgWb3ELi', 'j8hF7bzn06zLR3ChudEmgR5InA3uEdOopvKtRdkTmZ2qt')    
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

#I create a user object of my target account that has 250 followers
roca = api.get_user('JofreRocabert')

#One degree of separation:
####Among the followers of your target who is the most active?

target_followers = []
for page in tweepy.Cursor(api.followers_ids, screen_name="JofreRocabert").pages():#get followers id
    target_followers.extend(page)
    time.sleep(60)

print len(target_followers)#250 followers

status_followers = []
for i in range(0, len(target_followers)):#get number of statuses for each of the followers
    status_followers.append(api.get_user(target_followers[i]).statuses_count)

print len(status_followers)    
    
max_status = max(status_followers)#get max number of statuses in the list of followers
max_index = status_followers.index(max_status)#get its index so that I can look it up
n = api.get_user(target_followers[max_index]).name
n2 = api.get_user(target_followers[max_index]).screen_name

print "The most active follower of this account is %s (%s) with %d total statuses." % (n, n2, max_status)
#The most active follower of this account is Sergi CJ (SCristobalJane) with 105647 total statuses.


####Among the followers of your target who is the most popular, i.e. has the greatest number of followers?

followercount_followers = []#get the number of followers for each follower in the list
for i in range(0, len(target_followers)):
    followercount_followers.append(api.get_user(target_followers[i]).followers_count)
    print len(followercount_followers)

print len(followercount_followers) 

max_followers = max(followercount_followers)#repeated what I did above for statuses
max_index2 = followercount_followers.index(max_followers)
n3 = api.get_user(target_followers[max_index2]).name
n4 = api.get_user(target_followers[max_index2]).screen_name

print "The most popular follower of this account is %s with %d total followers." % (n3, max_followers)
#The most popular follower of this account is BlackHalt with 345778 total followers.


####Among the friends of your target, i.e. the users she is following, who are the most active layman, expert and celebrity?

target_friends = []
for page in tweepy.Cursor(api.friends_ids, screen_name="JofreRocabert").pages():#get friends ids
    target_friends.extend(page)
    time.sleep(60)
print len(target_friends)# 850 friends

followercount_friends = []
for i in range(0, len(target_friends)):
    followercount_friends.append(api.get_user(target_friends[i]).followers_count)

print len(followercount_friends)

status_friends = []#number of status for all friends
for i in range(0, len(target_friends)):
    status_friends.append(api.get_user(target_friends[i]).statuses_count)

status_celfriends = []
status_exfriends = []
status_layfriends = []

for i in range(0, len(target_friends)):
    if followercount_friends[i] >= 1000:
        status_celfriends.append(status_friends[i])
    elif followercount_friends[i] < 1000 and followercount_friends[i] >= 100:
        status_exfriends.append(status_friends[i])
    else:
        status_layfriends.append(status_friends[i])

maxst_layfriends = max(status_layfriends)
maxst_exfriends = max(status_exfriends)
maxst_celfriends = max(status_celfriends)

i = 0
for i in range(0, len(status_friends)):
    if maxst_celfriends == status_friends[i]:
        a1 = i
        print i
#index 681 is the max of status in the friends of the target account
n5 = api.get_user(target_friends[a1]).name
s5 = api.get_user(target_friends[a1]).statuses_count
print "The most active celebrity friend of this account is %s with %d total statuses." % (n5, s5)
#The most active celebrity friend of this account is The Guardian with 369469 total statuses.

i = 0
for i in range(0, len(status_friends)):
    if maxst_exfriends == status_friends[i]:
        a2 = i
        print i
#index 85 is the max of status in the friends of the target account
n6 = api.get_user(target_friends[a2]).name
s6 = api.get_user(target_friends[a2]).statuses_count
print "The most active expert friend of this account is %s with %d total statuses." % (n6, s6)
#The most active expert friend of this account is Jaume Sampériz with 44413 total statuses.

i = 0
for i in range(0, len(status_friends)):
    if maxst_layfriends == status_friends[i]:
        a3 = i
        print i

#index 752 is the max of status in the friends of the target account
n7 = api.get_user(target_friends[a3]).name
n27 = api.get_user(target_friends[a3]).screen_name
s7 = api.get_user(target_friends[a3]).statuses_count
print "The most active lay friend of this account is %s (%s) with %d total statuses." % (n7, n27, s7)
#The most active lay friend of this account is Внимательно слушаю. (sarguzinairsen) with 3528 total statuses.


####Among the friends of your target who is the most popular?

maxfoll_friends = max(followercount_friends)

i = 0
for i in range(0, len(status_friends)):
    if maxfoll_friends == followercount_friends[i]:
        a4 = i
        print i

#index 752 is the max of status in the friends of the target account
n8 = api.get_user(target_friends[a4]).name
n28 = api.get_user(target_friends[a4]).screen_name
s8 = api.get_user(target_friends[a4]).followers_count
print "The most popular friend of this account is %s with %d total followers." % (n8, s8)
#The most popular friend of this account is Barack Obama with 93855582 total followers.

#########Two degrees of separation: For the following two questions,
#########limit your search of followers and friends to laymen and experts.

####Among the followers of your target and their followers, who is the most active?

i = 0
target_followers2 = []
for i in range(0, len(target_followers)):
    if followercount_followers[i] <= 1000:
        target_followers2.append(target_followers)
    else:
        pass

#This is just to check. Yes, there are 137 followers of the target account who are not celebrities
len(target_followers2)
sum(float(num) <= 1000 for num in followercount_followers)

#Get followers of followers who are not celebrities
all_followers = []
for i in range(0, len(target_followers2)):
    try:
        for page in tweepy.Cursor(api.followers_ids, id=target_followers2[i]).pages():#get followers of the followers
            all_followers.extend(page)
            print len(all_followers)
    except TweepError as e:
        if 'Failed to send request:' in e.reason:
            print "Time out error caught."
            time.sleep(180)
            continue

#Add followers of the target account to the followers of followers
all_followers2 = all_followers + target_followers2

len(target_followers2)
len(all_followers)
len(all_followers2)

statusescount_allfollowers = []#get the number of statuses for each follower in the list

for i in range(0, len(all_followers2)-1):
    statusescount_allfollowers.append(api.get_user(all_followers2[i]).statuses_count)
    print len(statusescount_allfollowers)

print len(all_followers2)
print len(statusescount_allfollowers)

max_statuses_follo = max(statusescount_allfollowers)#get max value in the list
max_index2 = followercount_all.index(max_status_follo)#get index of max value
n3 = api.get_user(all_followers2[max_index2]).name#get name for the index
n4 = api.get_user(all_followers2[max_index2]).screen_name#get name for the index

print "The most active of the followers and followers of follwers of the target account is %s with %d total statuses." % (n3, max_followers)


####Among the friends of your target and their friends, who is the most active?

i = 0
target_friends2 = []
for i in range(0, len(target_friends)):
    if followercount_friends[i] <= 1000:
        target_friends2.append(target_friends)
    else:
        pass

#This is just to check. Yes, there are XXX friends of the target account who are not celebrities
len(target_friends2)
sum(float(num) <= 1000 for num in followercount_friends)

#Get friends of friends who are not celebrities
all_friends = []
for i in range(0, len(target_friends2)):
    for page in tweepy.Cursor(api.followers_ids, id=target_friends2[i]).pages():#get followers of the followers
        all_friends.extend(page)
        time.sleep(60)

all_friends2 = target_friends2 + all_friends

statusescount_all_friends = []#store here the number of statuses for each friend in the list

for i in range(0, len(all_friends2)-1):
    statusescount_all_friends.append(api.get_user(all_friends2[i]).statuses_count)

print len(all_friends2)
print len(statusescount_all_friends)

max_friends = max(statusescount_all_friends)#get max value in the list
max_index2 = all_friends2.index(max_friends)#get index of max value
n3 = api.get_user(all_friends2[max_index2]).name#get name for the index
n4 = api.get_user(all_friends2[max_index2]).screen_name#get name for the index

print "The most active of the friends and friends of friends of the target account is %s with %d total statuses." % (n3, max_friends)
