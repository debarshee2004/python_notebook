import sqlite3

# Establish a connection to the SQLite database and create a cursor object
con = sqlite3.connect("youtube_videos.db")
cur = con.cursor()

# Create the 'videos' table if it does not exist
cur.execute(
    """
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """
)


def listAllVideos():
    """
    Retrieve and print all records from the 'videos' table.
    """
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)


def addVideo():
    """
    Prompt the user to enter details for a new video and insert it into the 'videos' table.
    """
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def updateVideo():
    """
    List all videos, prompt the user to enter the ID of a video to update,
    and update the video's details in the 'videos' table.
    """
    listAllVideos()
    video_id = input("Enter the id of the video: ")
    new_name = input("Enter the new name of the video: ")
    new_time = input("Enter the new time of the video: ")
    cur.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def deleteVideo():
    """
    Prompt the user to enter the ID of a video and delete the corresponding
    record from the 'videos' table.
    """
    video_id = input("Enter the id of the video: ")
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    """
    Main function to run the YouTube Manager App, providing options to list,
    add, update, or delete videos, or exit the application.
    """
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
                listAllVideos()
            case "2":
                addVideo()
            case "3":
                updateVideo()
            case "4":
                deleteVideo()
            case "5":
                break
            case _:  # Default
                print("Invalid Input")
    con.close()


if __name__ == "__main__":
    main()
