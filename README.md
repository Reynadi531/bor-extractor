# BOR Extractor

BOR (Bed Occupancy Rate) Extractor from PDF table to csv file

- To build the docker file use:
    ```bash
    docker build . -t <image name>
    ```
- To run it:
  ```
  docker pull reynadi17/bor-extractor
  docker run --rm -v $PWD/tables:/app/tables reynadi17/bor-extractor
  ```

- Variable that could be passed
  * DATE: Default to today date and require value in range 1 - 31
  * MONTH: Default to today month and require value in range 1 - 12
  * YEAR: Default to today year and reuqire value above or equal to 2020
  ```bash
  docker run --rm \
   -v $PWD/tables:/app/tables \
   -e "DATE=24" \
   reynadi17/bor-extractor
  ```

### Data source
> https://www.kemkes.go.id/downloads/resources/download/Ketersediaan-Tempat-Tidur-RS-Covid19/

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

**[MIT license](http://opensource.org/licenses/mit-license.php)**