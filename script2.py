from youtube_transcript_api import YouTubeTranscriptApi


def textgenerator(urlid):
    List = []
    # ytt_api = YouTubeTranscriptApi()
    # fetched_script = ytt_api.fetch(urlid)
    # for snippet in fetched_script:
    #     List.append(snippet.text)
    ytt_api = YouTubeTranscriptApi()

    # retrieve the available transcripts
    transcript_list = ytt_api.list(urlid)
    transcript = transcript_list.find_generated_transcript(["en", "hi"])
    fetched_transcript = transcript.fetch()
    for snippet in fetched_transcript:
        List.append(snippet.text)

    return List
