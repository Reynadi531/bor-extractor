# BOR Extractor

BOR (Bed Occupancy Rate) Extractor from PDF table to csv file

- To build the docker file use:
    ```bash
    docker buld . -t <image name>
    ```
- To run it:
  ```
  docker pull reynadi17/bor-extractor
  docker run <imagename> -v path:/app/tables
  ```

### Data source
> https://www.kemkes.go.id/downloads/resources/download/Ketersediaan-Tempat-Tidur-RS-Covid19/
