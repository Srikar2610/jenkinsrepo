def main():
    print("Hello, Jenkins!")
    with open("output.txt", "w") as f:
        f.write("Jenkins Pipeline Successfully Executed!")

if __name__ == "__main__":
    main()
