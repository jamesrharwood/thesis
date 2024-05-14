.SECONDARY:

preview: pre_render
	@quarto preview --watch-inputs

preview_int: pre_render
	@quarto preview --no-browser --watch-inputs

publish: render add_footer
	@quarto publish gh-pages --no-render

pre_render: create_vars create_tables create_appendix

post_render: update_wordcounts

render: pre_render actual_render post_render

actual_render: 
	@echo 'Rendering...'
	@quarto render

create_tables:
	@echo 'Creating tables...'
	@python -m chapters.10_pilot.data.create_methods_table

create_appendix: 
	@echo 'Creating appendix...'
	@bash chapters/appendix/create_appendix.sh

commitID = $(shell git rev-parse --short --verify HEAD)
date = $(shell date)
file_ = metadata/_footer.yml
add_footer: check_commit
	@echo 'Altering footer...'
	@echo 'website:\n  page-footer:\n    center: "Updated: $(date) - Commit ID: $(commitID)"' > $(file_)
	@echo 'format:\n  docx:\n    date: now\n    author: "Commit ID: $(commitID)"' >> $(file_)

check_commit:
	@echo 'Checking for uncommitted changes...'
	@git update-index --refresh
	@git diff-index --quiet HEAD -- || (echo "There are uncommitted edits"; exit 1)

create_vars:
	@echo 'Creating variables...'
	@python create_variables.py

update_wordcounts:
	@echo 'Updating wordcounts...'
	@bash metadata/wordcounts.sh