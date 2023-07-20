preview:
	@quarto preview

render: add_footer
	@quarto render

check_commit:
	@git diff-index --quiet HEAD -- || (echo "There are unstaged commits"; exit 1)
	@echo "All changes are committed"

commitID = $(shell git rev-parse --short --verify HEAD)
date = $(shell date)
file_ = metadata/_footer.yml
add_footer: check_commit
	@echo 'website:\n  page-footer:\n    center: "Created: $(date) - Commit ID: $(commitID)"' > $(file_)
	@echo 'format:\n  docx:\n    date: "$(date) - Commit ID: $(commitID)"' >> $(file_)
