## Usage

Use scripts inside this directory to preprocess the given set of genome sequences.

### Steps
1. Edit `startup.properties` to give Genome source and kmer output directories.

2. Execute the bash script inside the bin directory of DSK-tool.

    ```bash
    sh kmer_listing.sh
    ```

3. Make sure to keep both properties and script files inside the DSK tool bin directory in the same level.

4. Use `txt_to_CSV_convertor.py` script to convert the output.txt files to .CSV format.

5. Use `dsk_tool_kmer_result_split.py` script to create the serialized specie with kmer objects.