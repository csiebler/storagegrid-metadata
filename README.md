# StorageGRID Metadata Search Stack

## Introduction

Description to follow!

The containerized setup is based on:

* A python-based indexing service
* Elasticsearch
* A Sinatra-based web search application

## Configuration

At this point in time, the StorageGRID Audit Logs need to be mounted on the Docker host under `/mnt/auditlogs/`

## Usage

* Start the stack via `./startup.sh`
* Terminte the stack via `./shutdown.sh`

The web search application is accessible via `http://<dockerhost>:8080/`.

## Notes
This is not an official NetApp repository. NetApp Inc. is not affiliated with the posted examples in any way.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
