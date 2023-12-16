OUTPUT_FP="metadata/_wordcounts.qmd"
echo "" > $OUTPUT_FP
total=0
totalWithoutTables=0

FILEPATHS=(
    "output/chapters/1_introduction"
    "output/chapters/2_reflexivity"
    "output/chapters/3_synthesis"
    "output/chapters/4_survey_content"
    "output/chapters/5_website_audit"
    "output/chapters/6_bcw"
    "output/chapters/7_workshops"
    "output/chapters/8_focus_groups"
    "output/chapters/9_defining_content"
    "output/chapters/10_redesign"
    "output/chapters/11_pilot"
    #"output/chapters/discussion"
)

for dir in ${FILEPATHS[@]}
do
    file=$( (find $dir -name 'JH*.docx') 2>&1 )
    if [ -z "$file" ];
    then
        echo "No docx file for $dir"
        continue
    else
        counts=$( (quarto pandoc --lua-filter filters/wordcount.lua $file | sed -n 1p; ) 2>&1 )
        echo $counts
        countarray=($counts)
        wordcount=${countarray[0]}
        tablewords=${countarray[1]}
        tablecount=${countarray[2]}
        figurecount=${countarray[3]}
        filepath=$file
        filename=${filepath##*/}
        filename=${filename%.docx}
        wordcountWithoutTables=$(($wordcount - $tablewords))
        #(basename "$filepath") 2>&1
        #filename="$(basename -- $filepath)" 2>&1
        chaptername="${filename/JH-chapter-/}"
        chaptername="${chaptername/.docx/}"
        echo "* $chaptername: $wordcountWithoutTables (inc. tables: $wordcount)" >> $OUTPUT_FP
        total=$(($total + $wordcount))
        totalWithoutTables=$(($totalWithoutTables + $wordcountWithoutTables))
    fi
    #echo ""
done
echo "" >> $OUTPUT_FP
echo "**TOTAL: $totalWithoutTables (inc. tables: $total)**" >> $OUTPUT_FP