preview:
	@quarto preview

publish: create_vars render 
	@quarto publish gh-pages --no-render

render: add_footer update_wordcounts
	@quarto render

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