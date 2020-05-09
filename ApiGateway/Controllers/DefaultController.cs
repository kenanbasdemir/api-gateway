using Microsoft.AspNetCore.Mvc;

namespace ApiGateway.Controllers
{

    [ApiController]
    [Route("api/[controller]")]
    public class DefaultController : ControllerBase
    {

        [HttpGet]
        public ActionResult<string> Get()
        {
            return "OK";
        }
    }
}