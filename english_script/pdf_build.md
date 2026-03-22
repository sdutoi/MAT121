## Quick start (PDF build)

- Move into your project folder and build the PDF:
```bash
cd /Users/stefandutoit/MAT121/english_script
latexmk -pdf -interaction=nonstopmode -halt-on-error analysis_1_and_2.tex
```

- Open the resulting PDF on macOS:
```bash
open analysis_1_and_2.pdf
```

Notes:
- -pdf tells latexmk to produce a PDF via pdflatex.
- -interaction=nonstopmode keeps the run going through non-fatal issues.
- -halt-on-error stops on a fatal error (so you don’t miss it).

## Live preview (auto rebuild on save)

- Continuous preview and rebuild:
```bash
latexmk -pdf -pvc -interaction=nonstopmode -halt-on-error analysis_1_and_2.tex
```
- -pvc = “preview continuously.” Latexmk watches files and rebuilds on save. Your default PDF viewer will auto-refresh when possible.

Stop with Ctrl+C.

## Cleaning aux files

- Clean intermediate files (keep the PDF):
```bash
latexmk -c
```

- Full clean (remove everything latexmk created, including the PDF):
```bash
latexmk -C
```

## Troubleshooting tips

- Verify binaries are available:
```bash
which latexmk
which pdflatex
```
If latexmk isn’t found, install MacTeX (includes latexmk). For a lighter install, BasicTeX + tlmgr install latexmk works too:
```bash
# After installing BasicTeX:
sudo tlmgr update --self
sudo tlmgr install latexmk
```

- Find errors quickly in the log:
```bash
grep -n "!" analysis_1_and_2.log
```
That jumps to TeX error lines; then open the `.log` to see context.

- When things get weird (stale aux files), do a quick reset:
```bash
latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error analysis_1_and_2.tex
```

## Optional: make “one-command” builds easier

If you want, I can add one of these to your repo (just say the word):
- Makefile:
  - make: build PDF
  - make watch: live preview
  - make clean: clean aux files
- .latexmkrc:
  - Sets default options so you can just run latexmk with no flags.

Example Makefile (optional, for reference only):
```make
# Optional Makefile
TEX=analysis_1_and_2.tex
PDF=$(TEX:.tex=.pdf)

all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(TEX)

watch:
	latexmk -pdf -pvc -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	latexmk -c

distclean:
	latexmk -C
```

