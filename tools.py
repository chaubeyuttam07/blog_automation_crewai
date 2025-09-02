from youtubesearchpython import VideosSearch

class YoutubeChannelSearchTool:
    def __init__(self, youtube_channel_handle):
        self.channel = youtube_channel_handle

    def search(self, topic):
        query = f"{topic} site:youtube.com {self.channel}"
        videosSearch = VideosSearch(query, limit=2)
        return videosSearch.result()



yt_tools = YoutubeChannelSearchTool(youtube_channel_handle='@krishna_yt')