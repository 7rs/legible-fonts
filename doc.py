def main():

    from docs import markdown

    with open("dist/configurator-doc.md", "w") as f:
        import configurator

        f.write(markdown.get_package_docs(configurator))

    with open("dist/generator-doc.md", "w") as f:
        import generator

        f.write(markdown.get_package_docs(generator))


if __name__ == "__main__":
    main()
