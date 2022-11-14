import logging

log = logging.getLogger(__name__)

def main(args):
    log.info("{}".format(args).replace(', ', ',\n'))
    for iter in range(args.iters):
        log.info(f"iter: {iter}")
        log.info(f"sleeping for: {args.iter_time}")
        import time
        for i in range(args.iter_time):
            log.info(i)
            time.sleep(1)
    log.info("Done")