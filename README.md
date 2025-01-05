# cosmo-crawl

`cosmo-crawl` is a repository that builds **Dungeon Crawl Stone Soup** using [Cosmopolitan Libc](https://justine.lol/cosmopolitan/). The result is a self-contained `crawl.com` binary that can run on multiple operating systems and architectures without requiring external dependencies.

- **Cross-Platform**: Single executable runs on Linux, macOS, Windows, FreeBSD, OpenBSD (<= 7.3), NetBSD.

- **Self-Contained**: No additional libraries or runtime dependencies are required, with all DCSS assets bundled into the executable.

- **Multi-Architecture**: Runs on both x86_64 and arm64.

## Download  

Prebuilt binaries can be found on the [Releases](https://github.com/bjia56/cosmo-crawl/releases) page. Releases are tagged using the format `major.minor.patch.build`, where:  
- `major.minor.patch` corresponds to the upstream Dungeon Crawl Stone Soup version.  
- `build` is an incremental build number for this repository.  

Example:  
- Tag `0.32.1.2` corresponds to Dungeon Crawl Stone Soup version `0.32.1` with the second build of `cosmo-crawl`.

## License  

This repository is licensed under the **CC0-1.0 License**. Note that Dungeon Crawl Stone Soup itself is distributed under its own license. Please refer to the upstream [Dungeon Crawl Stone Soup repository](https://github.com/crawl/crawl) for more information.  
