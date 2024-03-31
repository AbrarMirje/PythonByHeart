import sqlite3

con = sqlite3.connect('youtube_manager.db')

cursor = con.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL
                )
               ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?,?)", (name, time))
    con.commit()

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print('\nYouTube Manager App With DB')
        print('1. List videos')
        print('2. Add videos')
        print('3. Update videos')
        print('4. Delete videos')
        print('5. Exit App')

        choice = input('Enter your choice: ')
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_videos(name, time)
            case '3':
                video_id = input('Enter video id to update: ')
                name = input('Enter new video name: ')
                time = input('Enter new video time: ')
                update_videos(video_id, name, time)
            case '4':
                video_id = input('Enter video id to delete: ')
                delete_videos(video_id)
            case '5':
                break
            case _:
                print('Invalid Choice')
    con.close()
if  __name__ == '__main__':
    main()