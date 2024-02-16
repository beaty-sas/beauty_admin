import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('beauty_admin').version

except pkg_resources.DistributionNotFound:
    __version__ = 'unknown'
