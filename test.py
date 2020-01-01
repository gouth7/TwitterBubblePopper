import urllib2
import re

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False

def get_user_info(user_id):
    try:
        json_data = urllib2.urlopen('https://api.twitter.com/1.1/users/lookup.json?user_id=783214,6253282')
        found_ids = re.findall(r'screen_name=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False

print get_user_ids_of_post_likes(1179910004637237248)
#print get_user_info(12)

# Example:
# https://twitter.com/golan/status/731770343052972032


# ['13520332', '416273351', '284966399']
#
# 13520332 +> @TopLeftBrick
# 416273351 => @Berenger_r
# 284966399 => @FFrink
