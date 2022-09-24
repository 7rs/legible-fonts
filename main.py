import generator


def generate_font(generate_sfd: bool):
    if generate_sfd:
        generator.generate_sfd_files()
    generator.merge_sfd_files()


def main():
    generate_font(generate_sfd=False)


if __name__ == "__main__":
    main()
