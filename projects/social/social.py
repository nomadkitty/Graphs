import random
import time


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
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

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # make a list with all POSSIBLE friendships
        # Examples:
        # 5 users:
        # [(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5),(3,4), (3,5), (4,5)]
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)
        # Shuffle the list
        self.fisher_yates_shuffle(friendships)
        # Take as many as we need
        total_friendships = num_users * avg_friendships
        random_friendships = friendships[:total_friendships//2]
        # add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)

        # linear way to add the number of friendships we need?
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0
        # as long as we haven't made all the friendships we need
        while friendships_created < target_number_friendships:
            # pick 2 random numbers between 1 and the last id
            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)
        # try to create that friendship
            friendships_was_made = self.add_friendship(friend_one, friend_two)
        # if we can, increment friendship
            if friendships_was_made:
                friendships_created += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        Plan: BFT, 
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()

        # !!!! IMPLEMENT ME
        queue.enqueue([user_id])
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node not in visited:
                visited[current_node] = current_path
                neighbors = self.friendships[current_node]
                for neighbor in neighbors:
                    new_path = current_path + [neighbor]
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    num_users = 1000
    avg_friendships = 900

    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print(f'Populate graph O(n^2): {end_time - start_time}')

    start_time = time.time()
    sg.linear_populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print(f'Populate linear graph O(n): {end_time - start_time}')
    # Trade off for linear graph: the more densely connected the graph, the harder it gets to find new connections randomly

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)

    # # What percentage of total users are in our extended social network?
    # # how many people we know, divided by how many people there are
    # print(f'{(len(connections)-1)/1000 * 100}%')

    # # What is the average degree of separation between a user and those in his/her extended network?
    # # average length of a path to each other
    # # traverse a user's extended connections, gather lengths, sum
    # total_lengths = 0
    # for friend in connections:
    #     total_lengths += len(connections[friend])
    # # divide by number of friends in connected component aka extended social network
    # print(f'Average degree of seperation: {total_lengths / len(connections)}')

    # n = [len(v) for k, v in connections.items() if k != 1]
    # print(sum(n) / len(n))
    # sum([len(connection) for connection in connections])/len(connections)
