"""
CRUD Operations using Python and Files.
"""

import json


def loadData(fileName):
    try:
        with open(fileName, "r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []


def saveData_Helper(fileName, videos):
    with open(fileName, "w") as file:
        json.dump(videos, file)


def listAllVideos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)


def addVideo(fileName, videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    saveData_Helper(fileName, videos)


def updateVideo(fileName, videos):
    listAllVideos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        saveData_Helper(fileName, videos)
    else:
        print("Invalid index selected.")


def deleteVideo(fileName, videos):
    listAllVideos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        saveData_Helper(fileName, videos)
    else:
        print("Invalid video index selected.")


def main():
    fileName = "youtube.txt"
    videos = loadData(fileName)
    while True:
        print("\nYouTube Manager App")

        print("1. List all youtube videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")

        choice = str(input("Enter your choice..."))

        match choice:
            case "1":
                listAllVideos(videos)
            case "2":
                addVideo(fileName, videos)
            case "3":
                updateVideo(fileName, videos)
            case "4":
                deleteVideo(fileName, videos)
            case "5":
                break
            case _:  # Default
                print("Invalid Input")


if __name__ == "__main__":
    main()
