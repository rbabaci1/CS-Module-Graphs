import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()
        # Add users
        for i in range(num_users):
            self.add_user(f"User_{i + 1}")

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.reset()
        # Add users
        for i in range(num_users):
            self.add_user(f"User_{i + 1}")

        collisions = 0
        for i in range(num_users * avg_friendships // 2):
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if not self.add_friendship(user_id, friend_id):
                collisions += 1
        print(f"Collisions: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        queue = deque()
        queue.append([user_id])

        while len(queue):
            current_path = queue.popleft()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path

                for friend in self.friendships[current_user]:
                    if friend not in visited:
                        new_path = list(current_path)
                        new_path.append(friend)
                        queue.append(new_path)
        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    # sg.populate_graph(1000, 3)
    sg.populate_graph_linear(1000, 3)
    connections = sg.get_all_social_paths(1)

    print(f"Friendships:\n {sg.friendships}\n")
    print(f"Connections:\n {connections}")
