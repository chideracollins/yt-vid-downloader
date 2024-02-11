from pytube import YouTube


def download_vid(url, save_path):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    stream_res = streams.first()
    print("Download Started...!")
    stream_res.download(output_path=save_path)
    print("Downloaded Successfully!")


if __name__ == "__main__":
    url = "a url"
    save_path = "a save path"
    download_vid(url, save_path)
