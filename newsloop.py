from telethon.sync import TelegramClient
import requests
import json
import telethon
import os
import re
import time
from telethon.tl import types
import telethon.tl.types
from telethon.tl import types, functions
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session

# telegram API

api_id = 'telegrahmahs'
api_hash = 'hashyob'

# stack A

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=65268d14e2b2971be6db3478&org=67bf663c-07f6-4335-bf4e-0ceb79570042"
headers = {'Authorization':
           'Bearer yourkeyyyyyyyyyyyyyyyy',
           'Content-Type': 'application/json'
           }


# backup_stackAI

API_URL_backup = "https://www.stack-inference.com/run_deployed_flow?flow_id=651278a0aafac65587e08ec3&org=dc95f1c4-e3bc-465a-9916-c0e5625c1718"
headers_backup = {'Authorization':
                  'Bearer yourkeyyyyyyyyyyyyyyyy',
                  'Content-Type': 'application/json'
                  }


API_URL2 = "https://www.stack-inference.com/run_deployed_flow?flow_id=650e94a95a16985808c6916c&org=82901108-5b57-4bb0-aeb4-a94114e7edd0"
headers2 = {'Authorization':
            'Bearer c52yourkeyyyyyyyyyyyyyyyy',
            'Content-Type': 'application/json'
            }


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("STACK API CALL DATA")
    print(API_URL)
    print(headers)
    print(json)
    print("STACK API CALL DATA END")
    return response.json()


def query_b(payload):
    response = requests.post(
        API_URL_backup, headers=headers_backup, json=payload)
    print("STACK API CALL DATA")
    # print(API_URL)
    # print(headers)
    # print(json)
    print("STACK API CALL DATA END")
    return response.json()


def download_progress_callback(current, total):
    print(f"Downloaded: {current} bytes out of {total} bytes")


def query_for_summary(payloadd):

    response = requests.post(API_URL2, headers=headers2, json=payloadd)
    print(response)
    mst2 = str(response.json())
    print(response)
    modified_string2 = mst2[11:]
    modified_string2 = modified_string2[:-2]
    print("ammo hutto")
    print(modified_string2)
    return modified_string2


def init_twitter_media_upload():
    # Twitter API endpoint for media upload INIT command
    upload_url = "https://upload.twitter.com/1.1/media/upload.json"

    # Your Twitter API credentials
    api_key = ""
    api_secret_key = ""
    access_token = ""
    access_token_secret = ""

    # Create a Twitter OAuth 1.0a authentication session
    twitter = OAuth1Session(api_key, api_secret_key,
                            access_token, access_token_secret)

    # File details
    file_name = "video.mp4"  # Replace with your video file name
    file_path = os.path.join(os.path.dirname(
        __file__), file_name)  # Create the full file path
    # Get the total file size in bytes
    total_bytes = os.path.getsize(file_path)
    media_type = "video/mp4"  # MIME type for video files

    # Create the INIT request parameters
    params = {
        "command": "INIT",
        "total_bytes": total_bytes,
        "media_type": media_type
    }

    # Make the INIT request
    init_response = twitter.post(upload_url, params=params)

    # Check if the request was successful
    if init_response.status_code == 202:
        # Parse the response JSON
        init_data = init_response.json()

        # Get the media_id_string from the response
        media_id_string = init_data["media_id_string"]

        return media_id_string  # Return the media_id_string
    else:
        print("INIT upload failed with status code:", init_response.status_code)
        print("Response content:", init_response.text)
        return None  # Return None to indicate failure


# upload media to twitter

def upload_image_to_twitter(image_file):
    # Twitter API credentials
    consumer_key = ""
    consumer_secret = "CEgPKXYPaT"
    access_token = "1705234564RzFShqO9S2MmyJtcp54P6NCh"
    access_token_secret = "nVwveBHAUb5pdogwNhd8"

    # Authenticate with OAuth1
    auth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # Upload the image
    media_upload_url = "https://upload.twitter.com/1.1/media/upload.json?additional_owners=1705234564036116480"
    files = {'media': (image_file.name, image_file)}
    response = requests.post(url=media_upload_url, auth=auth, files=files)

    # Check for errors in the response
    if response.status_code == 200:
        try:
            media_id = response.json()['media_id']
            print("Media uploaded successfully. Media ID:", media_id)
            return media_id  # Return the media ID
        except ValueError:
            print("Error: Unable to parse JSON response.")
    else:
        print("Error:", response.status_code)

    return None  # Return None if there was an error


channel_username = 'latestnewsinusa'

channel_username5 = 'idfofficial'

channel_username2 = 'rtnews'

channel_username3 = 'vertigo_world_news'

channel_username4 = 'sputniknewsint'

channel_username1 = 'warmonitors'

last_message = "null"

lstyo = 'null'

validator = "hutto"
validator2 = "taghukanna"
validator3 = "test3"
validator4 = "test4"
tw_media_id = 0

counter = 0

media_status = 0

#  0 = no media
#  1 = photo
#  2 = video


while True:
    with TelegramClient('session_name', api_id, api_hash) as client:
        # Get the last message from the channel
        media_status = 0
        if counter % 6 == 0:
            last_message = client.get_messages(channel_username2, limit=1)[0]
        elif counter % 5 == 0:
            last_message = client.get_messages(channel_username3, limit=1)[0]
        elif counter % 2 == 0:
            last_message = client.get_messages(channel_username, limit=1)[0]
        else:
            last_message = client.get_messages(channel_username4, limit=1)[0]

        if 1 == 1:
            print("lessgaeg_text")
            input_string = last_message.message
            word_to_remove = "Subscribe"
            parts = input_string.split(word_to_remove, 1)
            result = parts[0]
            print(result)

        # Process the last message here
        print(f'Last message in the channel: {last_message.text}')

        file_name = 'photo.jpg'
        if last_message.media:
            if isinstance(last_message.media, types.MessageMediaPhoto):
                media_status = 1
                file_name = 'photo.jpg'
                client.download_media(last_message.media, file_name)
                print(f'Video downloaded and saved as {file_name}')
            elif isinstance(last_message.media, telethon.tl.types.MessageMediaDocument):
                if last_message.media.document.mime_type == 'video/mp4':
                    print(last_message.media.document.mime_type)
                    media_status = 2
                    print("testzoreo")
                    file_name = 'video.mp4'
                    client.download_media(
                        last_message.media,
                        file_name,
                        progress_callback=download_progress_callback
                    )
                    print(f'Video downloaded and saved as {file_name}')

    print("media Status")
    print(media_status)

    pattern = r'[^a-zA-Z\s]'

    print("checkerrr")
# Use re.sub() to remove symbols and marks
    # cleaned_string = re.sub(pattern, '', testtt)
    if counter % 2 == 0:
        testtt = f"""{last_message.text}"""
        testtt = re.sub(pattern, '', testtt)
        lstyo = last_message.text
        lstyo_five_chars = lstyo[:15]
        print(lstyo_five_chars)

        print(validator)

    else:
        testtt = f"""{last_message.text}"""
        testtt = re.sub(pattern, '', testtt)
        lstyo2 = last_message.text
        lstyo_five_chars = lstyo2[:15]
        print(lstyo_five_chars)
        print(validator2)

    if counter > 0:
        print("im here")

        if lstyo_five_chars == validator3 and counter % 6 == 0:
            print("not doing shit")

        elif lstyo_five_chars == validator4 and counter % 5 == 0:
            print("not doing shit")
        elif lstyo_five_chars == validator and counter % 2 == 0:
            print("do nothing")

        elif lstyo_five_chars == validator2 and counter % 2 > 0:
            print("not doing shit")

        else:
            output = query({"in-0": testtt})

            print(str(output))

            mst = str(output)

            modified_string = str(last_message.message)
            if "Subscribe to Sputnik" in modified_string:
                modified_string = modified_string.replace(
                    "Subscribe to Sputnik", "")
            if "Subscribe to RT" in modified_string:
                modified_string = modified_string.replace(
                    "Subscribe to RT", "")

            last_five_chars = modified_string[-5:]

            print(last_five_chars)
            if last_five_chars == 'error':
                print("skipping one loop du to stack ai auth error")
                continue

            print(modified_string)

            if media_status == 0:
                page_id_1 = 107854115729695
                facebook_access_token_1 = 'token long '
                msg = modified_string
                post_url = 'https://graph.facebook.com/{}/feed'.format(
                    page_id_1)
                payload = {
                    'message': msg,
                    'access_token': facebook_access_token_1
                }
                r = requests.post(post_url, data=payload)
                print(r.text)

            if media_status == 1:
                page_id_1 = 107854115729695
                facebook_access_token_1 = 'ong token'
                msg = modified_string
                media_filename = "photo.jpg"

    # Get the absolute path to the media file in the same directory as your code
                media_path = os.path.abspath(media_filename)

                # Open and read the media file as binary data
                with open(media_path, "rb") as media_file:
                    # Create a multi-part form data payload
                    files = {
                        # Adjust "image/jpeg" as needed for different file types
                        "file": (media_filename, media_file, "image/jpeg"),
                    }
                    payload = {

                        "message": modified_string,
                        "access_token": facebook_access_token_1,
                    }

                    post_url = f'https://graph.facebook.com/{page_id_1}/photos'

                    r = requests.post(post_url, data=payload, files=files)
                    print(r.text)
                    media_file.close()
                    # removed open media section
                    # Replace 'photo.jpg' with your image file path
                    image_file = open('photo.jpg', 'rb')
                    tw_media_id = upload_image_to_twitter(image_file)
                    print(tw_media_id)

            if media_status == 2:

                page_id_1 = 107854115729695
                facebook_access_token_1 = 'token'
                msg = modified_string
                media_filename = "video.mp4"

    # Get the absolute path to the media file in the same directory as your code
                media_path = os.path.abspath(media_filename)

                # Open and read the media file as binary data
                with open(media_path, "rb") as media_file:
                    # Create a multi-part form data payload
                    files = {
                        # Adjust "image/jpeg" as needed for different file types
                        "file": (media_filename, media_file, "video/mp4"),
                    }
                    payload = {
                        "description": modified_string,
                        "access_token": facebook_access_token_1,
                    }

                    post_url = f'https://graph.facebook.com/{page_id_1}/videos'
                    print(post_url)
                    print(payload)
                    r = requests.post(post_url, data=payload, files=files)
                    print(r)
                    # tw_media_id = upload_image_to_twitter(media_file)
                    print(r.text)
                    zirii = r.text
                    media_file.close()
                    # tw_media_id = init_twitter_media_upload()
                   # tw_media_id = upload_image_to_twitter(image_file)
                   # print(tw_media_id)

            # tweet

            if 0 == 0:

                url7 = "https://api.twitter.com/2/tweets"

                tweet_text = modified_string
                char_count = len(tweet_text)
                print("char count is")
                print(char_count)
                if char_count > 280:
                    print("sunarzirinf")
                    formattttttt = f"""{tweet_text}"""

                    output_summary = query_for_summary({"in-0": formattttttt})
                    print(output_summary)
                    tweet_text = output_summary
                    print(tweet_text)

                char_count = len(tweet_text)
                print("char count is")
                print(char_count)
                if char_count > 280:
                    print("sunarzirinf")
                    formattttttt = f"""{tweet_text}"""

                    output_summary = query_for_summary({"in-0": formattttttt})
                    print(output_summary)
                    tweet_text = output_summary
                    print(tweet_text)

# "media_ids": [media_id]
                # Create a dictionary with the tweet_text

                data = {
                    "text": tweet_text
                }

                # fuck having issues
                print("medoa ID")
                print(tw_media_id)
                tw_media_id = [tw_media_id]
                tw_media_id = [str(id) for id in tw_media_id]
               # integer_list = list(str(tw_media_id))
                if media_status == 9 or media_status == 1:
                    data = {
                        "text": tweet_text,
                        "media": {
                            "media_ids": tw_media_id
                        }
                    }

                # Convert the dictionary to JSON
                payload7 = json.dumps(data)
                headers7 = {
                    'Content-Type': 'application/json',
                    'Authorization': 'OAuth oauth_consumer_key="your key",oauth_token="1705234564036116480-sKVfqnRzFShqO9S2MmyJtcp54P6NCh",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1696677740",oauth_nonce="NVK69BiUq62",oauth_version="1.0",oauth_signature="FGsqbd%2BOC2L9jhJMtEBsa0UP7y8%3D"',
                    'Cookie': 'guest_id=v1%3A169574709531411779'
                }

                response = requests.request(
                    "POST", url7, headers=headers7, data=payload7)

                print(response.text)

                # experiment media tweet bitch

    if counter % 6 == 0:
        validator3 = lstyo_five_chars

    elif counter % 5 == 0:
        validator4 = lstyo_five_chars

    elif counter % 2 == 0:
        validator = lstyo_five_chars
    else:
        validator2 = lstyo_five_chars

    print(counter)
    delay_seconds = 900
    if counter < 5:
        delay_seconds = 10
    else:
        delay_seconds = 400

    counter += 1
    time.sleep(delay_seconds)
