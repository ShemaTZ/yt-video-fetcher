from googleapiclient.discovery import build
import json

def fetch_youtube_data(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    videos = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,
            order='date',
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                description = item['snippet']['description']
                date = item['snippet']['publishedAt']  # e.g., 2024-05-18T12:00:00Z
                year = int(date[:4])
                month = int(date[5:7])

                video_data = {
                    "id": video_id,
                    "title": title,
                    "description": description,
                    "embed": f"https://www.youtube.com/embed/{video_id}",
                    "year": year,
                    "month": month,
                    "category": "Bible"
                }

                videos.append(video_data)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

def main():
    api_key = input("Enter your YouTube API key: ")
    channel_id = input("Enter the YouTube Channel ID: ")

    print("Fetching videos...")
    videos = fetch_youtube_data(api_key, channel_id)

    with open('videos.json', 'w', encoding='utf-8') as f:
        json.dump({"videos": videos}, f, indent=2, ensure_ascii=False)

    print(f"Done! Saved {len(videos)} videos to videos.json.")

if __name__ == "__main__":
    main()
