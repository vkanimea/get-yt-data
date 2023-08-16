import os
import googleapiclient.discovery
import googleapiclient.errors

def get_youtube_data(search_keyword):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=search_keyword
    )
    response = request.execute()

    # TODO: Process the response to get the videos with the largest number of views, likes, and comments

if __name__ == "__main__":
    get_youtube_data("YOUR_SEARCH_KEYWORD")
