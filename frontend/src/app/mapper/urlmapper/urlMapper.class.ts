import { urls, urlsDTO } from "../../types/getapi.interface";

export class UrlMapper {
  public static dtoToUrl(singleUrl: urlsDTO): urls {
    return {
      id: singleUrl.id,
      createdAt: new Date(singleUrl.creation_date),
      clicks: singleUrl.clicks,
      code: singleUrl.short_url,
      url: singleUrl.original_url,
    };
  }
}
