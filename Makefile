.PHONY: all

render_single_doc:
	pandoc src/doc/*.md -o index.html
