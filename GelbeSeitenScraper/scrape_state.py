class ScrapeState:
    def __init__(self) -> None:
        with open("state.txt", "r") as state_file:
            lines = state_file.readlines()
            for i,line in enumerate(lines):
                lines[i] = float(line.split("=")[1].split("\n")[0]) if i == 3 else int(line.split("=")[1].split("\n")[0])
            self.found_emails = lines[0]
            self.unfound_emails = lines[1]
            self.completed_combinations = lines[2]
            self.time_passed = lines[3]

    def update_file(self):
        with open("state.txt", "w") as state_file:
            state_file.write(f"completed_combinations={self.completed_combinations}\nfound_emails={self.found_emails}\nunfound_emails={self.unfound_emails}\ntime_passed={self.time_passed}")  

    def increase_found_emails(self):
        self.found_emails+=1
        self.update_file()

    def increase_unfound_emails(self):
        self.unfound_emails+=1
        self.update_file()

    def increase_completed_combinations(self):
        self.completed_combinations+=1
        self.update_file()

    def increase_time_passed(self, time_to_add:float):
        self.time_passed+=time_to_add
        self.update_file()  