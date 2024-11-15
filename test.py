import yt_dlp

def download_video(link):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Requests the highest MP4 resolution.
            'merge_output_format': 'mkv',  # Ensures the final format is MP4.
            'outtmpl': '%(title)s.%(ext)s',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            }
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

link = input("Enter the link: ")
download_video(link)
