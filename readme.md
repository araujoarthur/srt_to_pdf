# SRT to PDF

Basic and very raw scripts to convert SRT files to PDF. Made to make it easier to study languages with movies/series subtitles.

There are no exception handling nor tests yet, but I do plan to improve the script in the future.

It uses [Jinja2](https://jinja.palletsprojects.com/) as templating tool to generate HTML and [WeasyPrint](https://weasyprint.org) to generate the pdf.

The following libraries are requirements of WeasyPrint:

- Cairo: 2D graphics library.
- Pango: Library for laying out and rendering text.
- GDK-PixBuf: Image loading library.
- Libffi: Foreign Function Interface library.
- Libxml2 and Libxslt: For XML and XSLT processing.

## Python Script Usage
<details>

<summary>Expand</summary>

### Configurations

<details>

<summary> <h3> MacOS </h3> </summary>

On MacOS one can install it through [Homebrew](https://brew.sh):
```
brew install cairo pango gdk-pixbuf libffi
```

>[!important]
>It's expected to have problems on MacOS when installing python from one source (e.g. universall installer provided by python.org) and WeasyPrint from another.

### Read this if you have problems with python not locating WeasyPrint's libraries
>[!info]
>This covers ARM macOS, because it's the only system I faced the problem.

1. Install python through [Homebrew](https://brew.sh)
```bash
brew install python
```
It's expected to prompt the installation of the latest version, or ask to reinstall if it's already installed.

2. Check `which python3`
Run the following command:
```bash
which python3
```

If it outputs a path outside brew's domain, it's likely you will need to update your `PATH` variable, otherwise you should be good already.

3. Updating the path variable.
Create or open your ``~/.zshrc`` file. I use code for that but you can also use nano. If you need to create it, run:
```bash
touch ~/.zshrc
```

Then there are the two options for editing

```bash
code ~/.zshrc
```

or

```bash
nano ~/.zshrc
```

Paste the following and save:

```bash
export PATH="/opt/homebrew/bin:$PATH"
```

Then just refresh your `PATH` variable. Once in terminal again, type:

```bash
source ~/.zshrc
```

</details>

</details>

## Got Malware'd?
Referencing the WeasyPrint's [documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation), sometimes it can be marked as malware, but it's not.
