![Untitled](https://github.com/pgrondein/etl_data_pipeline_airflow/assets/113172845/0b165796-9719-4177-87a1-9cecc3199419)
# Design of an ETL & Data Pipelines with Apache Airflow
Pipeline that analyzes the web server log file, extracts the required lines and fields, transforms, and load (append to an existing file.)

The script has to :
- Extract data from a web server log file
- Transform the data
- Load the transformed data into a tar file

The python script is here : [etl_pipeline_dag.py](https://github.com/pgrondein/etl_data_pipeline_airflow/blob/09fce008cebd6028dcf3a1cd920f5c9718206aa2/etl_pipeline_dag.py)

Then we can 
- ****Submit the DAG**** :

```markdown
cp process_web_log.py $AIRFLOW_HOME/dags
```

- ****Verify that our DAG got submitted****

```markdown
airflow dags list
```

- ****Unpause the DAG****

```markdown
airflow dags unpause process_web_log
```

- ****Monitor the DAG****
