# Yan_REU 

# Iterar sobre cada estrella
for position in star_positions:
    x, y = position
    
    # Definir las aperturas
    aperture = CircularAperture((x, y), r=radius_aperture)
    annulus_aperture = CircularAnnulus((x, y), r_in=radius_inner_annulus, r_out=radius_outer_annulus)
    apertures = [aperture, annulus_aperture]
    
    # Realizar fotometría de apertura
    phot_table = aperture_photometry(image_data, apertures)
    
    # Calcular fondo
    bkg_mean = phot_table['aperture_sum_1'] / annulus_aperture.area
    bkg_total = bkg_mean * aperture.area
    
    # Restar fondo
    net_star_flux = phot_table['aperture_sum_0'] - bkg_total
    
    # Calcular magnitud
    star_magnitude = -2.5 * np.log10(net_star_flux)
    
    # Llamar a la función calculate_photometry
    exptime = 60  # Tiempo de exposición de ejemplo
    flux_flag = True  # Indicador de flujo de ejemplo
    photometry_values = calculate_photometry(net_star_flux, aperture.area, annulus_aperture.area, std, exptime, flux_flag)
    
    # Mostrar resultados
    print(f'Estrella en posición {position}:')
    print(f'Flujo de estrella: {net_star_flux} e-/s')
    print(f'Magnitud de estrella: {star_magnitude}')
    print(f'Valores de fotometría: {photometry_values}\n')
