from pymongo import MongoClient
from bson import ObjectId

mongoURl = ""

# Initialize MongoDB client and database connection
client = MongoClient(
    mongoURl,
    tlsAllowInvalidCertificates=True,
)

print(client)
db = client["youtube_manager"]
video_collection = db["videos"]


def add_video(name, time):
    """
    Add a new video to the MongoDB collection.

    Args:
        name (str): The name of the video.
        time (str): The duration of the video.
    """
    video_collection.insert_one({"name": name, "time": time})


def list_videos():
    """
    List all videos from the MongoDB collection.
    """
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def update_video(video_id, new_name, new_time):
    """
    Update the details of a video in the MongoDB collection.

    Args:
        video_id (str): The ID of the video to update.
        new_name (str): The new name of the video.
        new_time (str): The new duration of the video.
    """
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}}
    )


def delete_video(video_id):
    """
    Delete a video from the MongoDB collection.

    Args:
        video_id (str): The ID of the video to delete.
    """
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    """
    Main function to run the YouTube Manager App, providing options to list,
    add, update, or delete videos, or to exit the application.
    """
    while True:
        print("\nYouTube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
