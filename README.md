# BOR Extractor

BOR (Bed Occupancy Rate) Extractor from PDF table to csv file

- To build the docker file use:
    ```bash
    docker build . -t <image name>
    ```
- To run it:
  ```bash
  docker run --rm -v $PWD/tables:/app/tables <image name>
  ```
- To run from premade image:
  ```bash
  docker pull reynadi17/bor-extractor
  docker run -e "DATE=30" reynadi17/bor-extractor
  ```

- Variable that could be passed
  * DATE: Default to today date and require value in range 1 - 31
  * MONTH: Default to today month and require value in range 1 - 12
  * YEAR: Default to today year and reuqire value above or equal to 2020
  ```bash
  docker run --rm \
   -v $PWD/tables:/app/tables \
   -e "DATE=24" \
   <image name>
  ```

### Data source
> https://www.kemkes.go.id/downloads/resources/download/Ketersediaan-Tempat-Tidur-RS-Covid19/

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

**[MIT license](http://opensource.org/licenses/mit-license.php)**
