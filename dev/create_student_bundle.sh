# Purpose:
#   * Generate a ZIP file that contains
#     the content from training-products
#     without the developer files
#     and without the .git/ content
#   * Assumes that this script is run from
#     within the /dev directory
#     i.e. $PWD must be /dev
#----------------------------------------

start_path=$PWD
cd ..
path_to_repo=$PWD
repo_name=training-products
old_path=$path_to_repo
echo "old path = $old_path"

new_dir=training_products_`date +"%Y%m%d_%H%M%S"`
new_path=$HOME/Desktop/$new_dir
echo "new path = $new_path"

echo "Copying $old_dir to $new_dir ..."
cp -R $old_path $new_path

#----------------------------------------
echo "Cleaning $new_dir ..."

cd $new_path

find . -name "*~" | xargs rm # remove emacs temp files
find . -name ".DS_Store" | xargs rm # remove OSX directory trash
find . -name ".ipynb_checkpoints" | xargs rm -rf
find . -type d -name "dev" | xargs rm -rf

rm -rf .git # remove git repo machinery, commit object store
rm -rf .gitignore

rm $new_path/Dask/log
rm $new_path/Dask/mydask.png

# Delete large data files that can be downloaded using
# ./data/master_downloads.py
rm -rf $new_path/data/Bokeh/*
rm -rf $new_path/data/BokehGeo/*
rm -rf $new_path/data/Datashader/*

#----------------------------------------
cd ..
zip_file=$new_dir.zip
zip_path=$HOME/Desktop
echo "Creating ZIP archive of $new_dir ..."

zip -r $zip_path/$zip_file $new_dir



#----------------------------------------
cd $start_path
echo "Done... your new deliverable is located here:"
echo "    $zip_path/$zip_file"





