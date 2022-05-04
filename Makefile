.PHONY: all

render_single_doc:
	pandoc main.md 01.md 02.md 03.md -o index.html
