import os
import logging

from reader import Reader


def parse_config_params():
    params = {
        'reviews_path': os.environ['REVIEWS_PATH'],
        'reviews_message_size': int(os.environ['REVIEWS_MESSAGE_SIZE']),
        'reviews_by_day_queue': os.environ['REVIEWS_BY_DAY_QUEUE'],
        'reviews_by_day_aggregators': int(os.environ['REVIEWS_BY_DAY_AGGREGATORS'])
    }
    return params


def main():
    initialize_log()
    logging.info("Starting reader")
    config_params = parse_config_params()
    logging.info("Reviews data is located at: {}".format(config_params['reviews_path']))
    reader = Reader(config_params['reviews_path'], config_params['reviews_message_size'],
                    config_params['reviews_by_day_queue'], config_params['reviews_by_day_aggregators'])
    reader.start()


def initialize_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )


if __name__ == "__main__":
    main()
