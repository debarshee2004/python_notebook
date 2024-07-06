import json


def loadData(fileName):
    """
    Load data from a JSON file. If the file does not exist, return an empty list.

    Args: fileName (str): The name of the file to load data from.

    Returns: list: The list of videos.
    """
    try:
        with open(fileName, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def saveData_Helper(fileName, videos):
    """
    Save data to a JSON file.

    Args:
        fileName (str): The name of the file to save data to.
        videos (list): The list of videos to save.
    """
    with open(fileName, "w") as file:
        json.dump(videos, file)


def listAllVideos(videos):
    """
    Print all videos in the list.

    Args: videos (list): The list of videos to print.
    """
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)


def addVideo(fileName, videos):
    """
    Prompt the user to enter a new video's name and duration, and add it to the list.

    Args:
        fileName (str): The name of the file to save data to.
        videos (list): The list of videos to update.
    """
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    saveData_Helper(fileName, videos)


def updateVideo(fileName, videos):
    """
    Prompt the user to select a video to update, and update its details.

    Args:
        fileName (str): The name of the file to save data to.
        videos (list): The list of videos to update.
    """
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
    """
    Prompt the user to select a video to delete, and remove it from the list.

    Args:
        fileName (str): The name of the file to save data to.
        videos (list): The list of videos to update.
    """
    listAllVideos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        saveData_Helper(fileName, videos)
    else:
        print("Invalid video index selected.")


def main():
    """
    Main function to run the YouTube Manager App, providing options to list,
    add, update, or delete videos, or to exit the application.
    """
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
