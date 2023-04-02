import bot
import ec2

def main():
    ec2.setup()
    bot.run()


if __name__ == "__main__":
    main()