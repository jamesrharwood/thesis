OUTPUT_FP="metadata/_wordcounts.qmd"
echo "" > $OUTPUT_FP
total=0

FILEPATHS=(
    #"output/chapters/1_introduction"
    #"output/chapters/2_reflexivity"
    "output/chapters/3_synthesis"
    "output/chapters/4_survey_content"
    "output/chapters/5_website_audit"
    #"output/chapters/6_journal_audit"
    "output/chapters/7_bcw"
    "output/chapters/8_workshops"
    "output/chapters/9_focus_groups"
    "output/chapters/10_redesign"
    "output/chapters/11_pilot"
    #"output/chapters/discussion"
)

for dir in ${FILEPATHS[@]}
do
    file=$( (find $dir -name '*.docx') 2>&1 )
    counts=$( (quarto pandoc --lua-filter filters/wordcount.lua $file | sed -n 1p; ) 2>&1 )
    countarray=($counts)
    wordcount=${countarray[0]}
    filepath=$file
    filename=${filepath##*/}
    filename=${filename%.docx}
    #(basename "$filepath") 2>&1
    #filename="$(basename -- $filepath)" 2>&1
    chaptername="${filename/JH-chapter-/}"
    chaptername="${chaptername/.docx/}"
    echo "* $chaptername: $wordcount" >> $OUTPUT_FP
    total=$(($total + $wordcount))
    #echo ""
done
echo "" >> $OUTPUT_FP
echo "**TOTAL: $total**" >> $OUTPUT_FP