import os
import googleapiclient.discovery
import googleapiclient.errors

def get_youtube_data(search_keyword):
    api_service_name = "youtube"
    api_version = "v3"
    with open('.YoutubeAPI', 'r') as file:
        DEVELOPER_KEY = file.read().strip()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=search_keyword
    )
    response = request.execute()

    video_stats = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        video_response = video_request.execute()
        video_stats.append({
            'id': video_id,
            'title': item['snippet']['title'],
            'viewCount': int(video_response['items'][0]['statistics']['viewCount']),
            'likeCount': int(video_response['items'][0]['statistics'].get('likeCount', 0)),
            'commentCount': int(video_response['items'][0]['statistics'].get('commentCount', 0)),
        })

    # Sort videos by view count, like count, and comment count in descending order
    video_stats.sort(key=lambda x: (x['viewCount'], x['likeCount'], x['commentCount']), reverse=True)

    # Print the videos with the largest number of views, likes, and comments
    for video in video_stats:
        print(f"Video ID: {video['id']}, Title: {video['title']}, Views: {video['viewCount']}, Likes: {video['likeCount']}, Comments: {video['commentCount']}")

if __name__ == "__main__":
    get_youtube_data("YOUR_SEARCH_KEYWORD")
