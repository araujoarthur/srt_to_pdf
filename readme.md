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

On MacOS one can install it through Homebrew:
```
brew install cairo pango gdk-pixbuf libffi
```

Referencing the WeasyPrint's [documentation](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation), sometimes it can be marked as malware, but it's not.
