from prefect.deployments import Deployment
from etl_web_to_gcs import etl_web_to_gcs
from prefect.filesystems import GitHub 

storage = GitHub.load("ghs-webtogcs")

deployment = Deployment.build_from_flow(
     flow=etl_web_to_gcs,
     name="github-deploy-block",
     storage=storage
     )

if __name__ == "__main__":
    deployment.apply()
