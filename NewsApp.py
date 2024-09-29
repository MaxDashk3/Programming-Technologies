import NewsQueue as nq

Queue = []

while True:
    print("Enter a command (without square brackets)\n"
          "To add news use \"add [name]:[content]\"\n"
          "To view all use \"view\"\n"
          "To pop the last use \"pop\"\n"
          "To get index of a news item use \"index [name]\"\n"
          "e to exit")
    user_input = input().partition(" ")
    match user_input[0]:
        case "add":
            title_and_content=user_input[2].split(":")
            Queue = nq.add(title_and_content[0], title_and_content[1], Queue)
            print("Added")
        case "view":
            nq.view_all(Queue)
        case "pop":
            nq.pop(Queue)
        case "index":
            print(nq.title_index(user_input[2], Queue))
        case "e":
            break
        case _:
            print("No such command!")