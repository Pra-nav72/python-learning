# class IndieMusic:
#
#     def __init__(self, songs):
#         self.song = songs
#
#     def playing(self):
#         print(f"playing song: {self.song}")
#
#
# class Premium(IndieMusic):  # inherited --> IndieMusic
#     def __init__(self, pod, songs):
#         self.pod = pod  # additional feature of podcast
#         super().__init__(songs)  # super constructor
#         print("PREMIUM Version")
#
#     def podcast(self):
#         print(f"podcast is playing: {self.pod}")
#
#
# a = IndieMusic("Khairiyat")
# a.playing()
# # a.podcast()  ----> error! cause no such attributes to object 'a'
#
# a2 = Premium("TRS", "sun raha hai na tu")
# a2.playing()
# a2.podcast()


class IndieMusic:

    def __init__(self):
        self._song = "ad"

    @property
    def song(self):
        # print("getter method called")
        return self._song

    @song.setter
    def song(self, name):
        # print("setter method called")
        self._song = name

    def playing(self):
        print(f"playing song: {self._song}")


class Premium(IndieMusic):  # inherited ---> IndieMusic
    def __init__(self):
        print("\nPREMIUM Version\n")
        super().__init__()  # super constructor ---> its variable called
        self._pod = "No podcast Available"

    @property
    def pod(self):
        return self._pod

    @pod.setter
    def pod(self, name):
        self._pod = name

    def podcast(self):
        print(f"playing podcast: {self._pod}")


user = input("Enter the name of the song:")
user2 = input("Enter the name of the podcast")

a = IndieMusic()
a.song = user
a.playing()

a2 = Premium()
a2.song = user
a2.pod = user2

a2.playing()
a2.podcast()
