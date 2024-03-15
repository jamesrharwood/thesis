preview: create_tables
	@quarto preview --watch-inputs

publish: render add_footer
	@quarto publish gh-pages --no-render

render: create_vars update_wordcounts create_tables create_appendix
	@quarto render

create_tables:
	@python -m chapters.10_pilot.data.create_methods_table

create_appendix: 
	@bash chapters/appendix/create_appendix.sh

commitID = $(shell git rev-parse --short --verify HEAD)
date = $(shell date)
file_ = metadata/_footer.yml
add_footer: check_commit
	@echo 'website:\n  page-footer:\n    center: "Updated: $(date) - Commit ID: $(commitID)"' > $(file_)
	@echo 'format:\n  docx:\n    date: now\n    author: "Commit ID: $(commitID)"' >> $(file_)

check_commit:
	@git update-index --refresh
	@git diff-index --quiet HEAD -- || (echo "There are uncommitted edits"; exit 1)

create_vars:
	@python create_variables.py

update_wordcounts:
	@bash metadata/wordcounts.sh