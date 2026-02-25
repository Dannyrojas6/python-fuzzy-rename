from pathlib import Path


def main():
    while True:
        media = Path(input("请输入媒体文件夹路径："))
        # media = Path(r"D:\VSCodeRepository\python-fuzzy-rename\media")
        video = sorted([file.name for file in media.iterdir() if file.suffix == ".mkv"])
        sub = sorted(
            [file.name for file in media.iterdir() if file.suffix in (".ass", ".srt")]
        )
        if len(video) != len(sub):
            print("视频与字幕文件数量不一致！程序已退出…………")
            break
        for i in range(len(video)):
            video_path = Path(media / video[i])
            sub_path = Path(media / sub[i])
            print(video_path)
            print(sub_path)
            format_sub_path = media / (video_path.stem + sub_path.suffix)
            sub_path.rename(format_sub_path)
        break


if __name__ == "__main__":
    main()
